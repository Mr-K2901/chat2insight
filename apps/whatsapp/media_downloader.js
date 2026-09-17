async function downloadMedia(message) {
  if (!message.hasMedia) return null;
  return message.downloadMedia();
}

module.exports = { downloadMedia };
