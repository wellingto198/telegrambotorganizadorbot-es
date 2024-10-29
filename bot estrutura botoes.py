from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Função para organizar os links recebidos
def organizar_links(links_text):
    links = links_text.strip().splitlines()
    estrutura = ""
    
    print(f"[LOG] Recebidos {len(links)} links para organização.")  # Log do número de links

    if len(links) > 5:
        # Para mais de cinco links, agrupa em dois links por linha com colchetes []
        for i in range(0, len(links), 2):
            link_1 = f"[{i + 1}ª Temporada - {links[i]}]"
            if i + 1 < len(links):
                link_2 = f"[{i + 2}ª Temporada - {links[i + 1]}]"
                estrutura += f"{{{link_1} {link_2}}}\n"  # Dois links por linha, ambos dentro de {}
            else:
                estrutura += f"{{{link_1}}}\n"  # Caso ímpar, último link sozinho dentro de {}
    else:
        # Para até cinco links, usa uma estrutura com chaves {} em linhas separadas
        for i, link in enumerate(links, start=1):
            estrutura += f"{{[{i}ª Temporada - {link}]}}\n"  # Cada link em uma linha com {}
    
    print(f"[LOG] Estrutura gerada:\n{estrutura}")  # Log da estrutura gerada
    return estrutura

# Comando de início
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Envie uma lista de links, um por linha, e eu organizarei por temporada!")

# Função que processa a mensagem com links
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    links_text = update.message.text
    if links_text:
        print("[LOG] Mensagem recebida com links.")  # Log para confirmar recebimento da mensagem
        estrutura_links = organizar_links(links_text)
        await update.message.reply_text(estrutura_links)
    else:
        print("[LOG] Mensagem recebida sem texto.")  # Log para mensagens sem texto
        await update.message.reply_text("Envie os links em uma mensagem de texto.")

# Configuração do bot
def main():
    # Insira seu token aqui
    TOKEN = '7565490897:AAGT5WCjjsnRSZSTIvRz_MpHN85-XpUZgqI'
    
    # Cria o aplicativo do bot com o token
    application = Application.builder().token(TOKEN).build()

    # Adiciona o comando /start
    application.add_handler(CommandHandler("start", start))

    # Adiciona o handler para mensagens de texto
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("[LOG] Bot iniciado e aguardando mensagens.")  # Log para indicar que o bot foi iniciado
    # Inicia o bot
    application.run_polling()

if __name__ == '__main__':
    main()
