async function listGroups(client) {
  const chats = await client.getChats();
  return chats.filter((chat) => chat.isGroup);
}

module.exports = { listGroups };
