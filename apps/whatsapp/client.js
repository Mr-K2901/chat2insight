const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');

function createWhatsAppClient() {
  const client = new Client({ authStrategy: new LocalAuth() });
  client.on('qr', (code) => qrcode.generate(code, { small: true }));
  client.on('ready', () => console.log('WhatsApp client is ready'));
  return client;
}

module.exports = { createWhatsAppClient };
