"""
MkDocs hook: publish llms.txt, llms-ctx.txt, llms-full.txt and the llms/ markdown files (cdm_tools.llms) with the
site.

The .txt files are added as generated site files, so that pages can link to them; the files under llms/ are written
after the build, because MkDocs would render markdown files as pages. Their absolute links use `extra.llms_base_url`
(falling back to `site_url`).
"""

from pathlib import Path

from mkdocs.exceptions import PluginError
from mkdocs.structure.files import File

from cdm_tools.llms import REPO_URL, build_llms, check_inputs, write_files
from cdm_tools.registry import RegistryError

SCHEMA = "src/common_data_model/schema/common_data_model.yaml"
REGISTRY = "src/docs/links/registry.yaml"
API_DIR = "src/docs/api"

_outputs: dict[str, str] = {}


def on_files(files, config):
    root = Path(config.config_file_path).parent
    schema, registry, api_dir = root / SCHEMA, root / REGISTRY, root / API_DIR
    problem = check_inputs(schema, registry, api_dir, config.docs_dir)
    if problem:
        raise PluginError(f"cdm-gen-llms: {problem}")
    base_url = config.extra.get("llms_base_url") or config.site_url
    if not base_url:
        raise PluginError("cdm-gen-llms: set extra.llms_base_url or site_url in mkdocs.yml")
    try:
        outputs = build_llms(schema, registry_path=registry, api_dir=api_dir, docs_dir=config.docs_dir,
                             repo_url=config.repo_url or REPO_URL, base_url=base_url)
    except RegistryError as exc:
        raise PluginError(f"cdm-gen-llms: invalid link registry: {exc}") from exc
    _outputs.clear()
    _outputs.update(outputs)
    for path, text in outputs.items():
        if "/" not in path:
            files.append(File.generated(config, path, content=text))
    return files


def on_post_build(config):
    write_files(config.site_dir, {path: text for path, text in _outputs.items() if "/" in path})
