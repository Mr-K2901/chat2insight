function configureAuth() {
  return { clientId: process.env.WHATSAPP_CLIENT_ID || 'chat2insight' };
}

module.exports = { configureAuth };
