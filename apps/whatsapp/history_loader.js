async function loadHistory(chat, limit = 100) {
  return chat.fetchMessages({ limit });
}

module.exports = { loadHistory };
