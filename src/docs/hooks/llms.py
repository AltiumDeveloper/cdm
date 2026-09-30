"""
MkDocs hook: publish llms.txt, llms-full.txt and the llms/ markdown files (cdm_tools.llms) with the site.

llms.txt and llms-full.txt are added as generated site files, so that pages can link to them; the files under llms/
are written after the build, because MkDocs would render markdown files as pages.
"""

from pathlib import Path

from mkdocs.structure.files import File

from cdm_tools.llms import build_llms, write_files

SCHEMA = "src/common_data_model/schema/common_data_model.yaml"
REGISTRY = "src/docs/links/registry.yaml"
API_DIR = "src/docs/api"

_outputs: dict[str, str] = {}


def on_files(files, config):
    root = Path(config.config_file_path).parent
    _outputs.clear()
    _outputs.update(build_llms(root / SCHEMA, registry_path=root / REGISTRY, api_dir=root / API_DIR,
                               docs_dir=config.docs_dir, repo_url=config.repo_url))
    for path, text in _outputs.items():
        if "/" not in path:
            files.append(File.generated(config, path, content=text))
    return files


def on_post_build(config):
    write_files(config.site_dir, {path: text for path, text in _outputs.items() if "/" in path})
