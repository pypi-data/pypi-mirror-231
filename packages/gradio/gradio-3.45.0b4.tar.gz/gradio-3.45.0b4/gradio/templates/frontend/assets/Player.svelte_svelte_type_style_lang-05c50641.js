const prettyBytes = (bytes) => {
  let units = ["B", "KB", "MB", "GB", "PB"];
  let i = 0;
  while (bytes > 1024) {
    bytes /= 1024;
    i++;
  }
  let unit = units[i];
  return bytes.toFixed(1) + " " + unit;
};
const playable = () => {
  return true;
};
function loaded(node, { autoplay }) {
  async function handle_playback() {
    if (!autoplay)
      return;
    await node.play();
  }
  node.addEventListener("loadeddata", handle_playback);
  return {
    destroy() {
      node.removeEventListener("loadeddata", handle_playback);
    }
  };
}

const Player_svelte_svelte_type_style_lang = '';

export { playable as a, loaded as l, prettyBytes as p };
//# sourceMappingURL=Player.svelte_svelte_type_style_lang-05c50641.js.map
