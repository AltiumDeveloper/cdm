// Copy buttons next to the IRI and GRID under a page title, shown on hover (document$ emits once per page load).
document$.subscribe(() => {
  document.querySelectorAll(".md-typeset .page-subtitle").forEach((line) => {
    const target = line.querySelector('a[href^="https://w3id.org/"], code');
    if (!target || line.querySelector(".copy-btn")) return;
    const button = document.createElement("button");
    button.type = "button";
    button.className = "copy-btn";
    button.title = "Copy to clipboard";
    button.setAttribute("aria-label", "Copy to clipboard");
    button.addEventListener("click", async () => {
      await navigator.clipboard.writeText(target.textContent.trim());
      button.classList.add("copied");
      setTimeout(() => button.classList.remove("copied"), 1200);
    });
    target.after(button);
  });
});
