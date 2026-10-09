// Exact versions: the floating mermaid@11 tag once moved to a release that broke every diagram on the site.
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11.17.0/dist/mermaid.esm.min.mjs';
import elkLayouts from 'https://cdn.jsdelivr.net/npm/@mermaid-js/layout-elk@0.2.3/dist/mermaid-layout-elk.esm.min.mjs';

// Diagram look shared with the site (custom.css): Inter, the site's greys for lines and text. Node fills come from the
// bounded-context colours set per diagram (class_diagram.md.jinja2), whose front matter sets the layout options.
const FONT = 'Inter, system-ui, -apple-system, "Segoe UI", sans-serif';

mermaid.registerLayoutLoaders(elkLayouts);
mermaid.initialize({
  startOnLoad: false,
  securityLevel: "loose",
  layout: "elk",
  theme: "base",
  fontFamily: FONT,
  themeVariables: {
    fontFamily: FONT,
    fontSize: "13px",
    primaryColor: "#f6f7f9",
    primaryBorderColor: "#98a1b3",
    primaryTextColor: "#14181f",
    textColor: "#3b4352",
    lineColor: "#98a1b3",
    edgeLabelBackground: "#ffffff",
    tertiaryColor: "#ffffff",
  },
});

// Diagrams carry the class cdm-diagram (mkdocs.yml), so Material's own mermaid integration leaves them alone. Each is
// rendered from its source text: the mermaid2 fence wraps it in a <code> element, and mermaid.run() reads an element's
// HTML (tags and entities included), which mangles it; mermaid.render() takes the text as is. bindFunctions attaches
// the node click links.
const diagrams = [...document.querySelectorAll(".cdm-diagram:not([data-processed])")];
diagrams.forEach(async (el, index) => {
  const source = (el.querySelector("code") || el).textContent;
  try {
    const { svg, bindFunctions } = await mermaid.render(`cdm-diagram-${index}`, source);
    el.innerHTML = svg;
    el.setAttribute("data-processed", "true");
    if (bindFunctions) bindFunctions(el);
    addExpand(el);
  } catch (error) {
    console.error(error);
  }
});

// Diagrams wider than the column are shown fitted to it; "Expand" opens one at its natural size in an overlay that
// scrolls. The diagram's own SVG is moved there and back, so its node links keep working. Esc or the backdrop closes.
function addExpand(el) {
  const svg = el.querySelector("svg");
  const natural = svg && svg.viewBox && svg.viewBox.baseVal ? svg.viewBox.baseVal.width : 0;
  if (!natural || natural <= el.clientWidth) return;
  const button = document.createElement("button");
  button.type = "button";
  button.className = "cdm-diagram__expand";
  button.textContent = "Expand";
  button.title = "Show the diagram at full size";
  button.addEventListener("click", () => openOverlay(el, svg, natural));
  el.appendChild(button);
}

function openOverlay(el, svg, natural) {
  const overlay = document.createElement("div");
  overlay.className = "cdm-diagram-overlay";
  overlay.innerHTML = '<div class="cdm-diagram-overlay__panel cdm-diagram" data-processed="true">' +
    '<button type="button" class="cdm-diagram-overlay__close" aria-label="Close">Close</button></div>';
  const panel = overlay.firstElementChild;
  const placeholder = document.createComment("diagram");
  const style = svg.getAttribute("style");
  svg.replaceWith(placeholder);
  svg.setAttribute("style", `max-width: none; width: ${natural}px; height: auto;`);
  panel.appendChild(svg);
  const close = () => {
    svg.setAttribute("style", style || "");
    placeholder.replaceWith(svg);
    overlay.remove();
    document.removeEventListener("keydown", onKey);
  };
  const onKey = (event) => { if (event.key === "Escape") close(); };
  overlay.addEventListener("click", (event) => { if (event.target === overlay) close(); });
  panel.querySelector(".cdm-diagram-overlay__close").addEventListener("click", close);
  document.addEventListener("keydown", onKey);
  document.body.appendChild(overlay);
}
