import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get the bot token from the environment variable
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

if not TOKEN:
    logger.error("No token provided. Please set the TELEGRAM_BOT_TOKEN environment variable.")
    raise ValueError("No token provided. Please set the TELEGRAM_BOT_TOKEN environment variable.")
logger.info(f"Bot token: {TOKEN}")

async def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message."""
    await welcome(update, context)
    
async def welcome(update: Update, context: CallbackContext) -> None:
    """Send a language selection message."""
    
    language_keyboard = [
        [InlineKeyboardButton("English", callback_data='language_en')],
        [InlineKeyboardButton("Amharic", callback_data='language_am')]
    ]
    reply_markup_language = InlineKeyboardMarkup(inline_keyboard=language_keyboard)
    await update.message.reply_text("Please select your language: \n እባክዎት የሚፈልጉትን ቋንቋ ይምረጡ:", reply_markup=reply_markup_language)

async def language_selected(update: Update, context: CallbackContext) -> None:
    """Set the selected language and display the main menu."""
    query = update.callback_query
    await query.answer()
    language = query.data
    context.user_data['language'] = language
    await query.message.delete()
    await main_menu(query.message.chat_id, context)
    
async def main_menu(chat_id: int, context: CallbackContext) -> None:
    """Display the main menu with options based on the selected language."""
    language = context.user_data.get('language', 'language_en')
    # Default to English if language is not set
    if language == 'language_en':
        options = {
            'payment_issue': "💳 Payment Issue Resolution",
            'how_to_guides': "📘 How-to Guides",
            'arif_volunteer': "💼 Arif Volunteer",
            'arif_intern': "🎓 Arif Intern",
            'arif_jobs': "🔧 Arif Jobs",
            'Other_supports': "🛟 Other Supports"
        }
    else:  # Amharic language
        options = {
            'payment_issue': "💳 የክፍያ ጉዳዮች",
            'how_to_guides': "📘 አጠቃቀም እና መመሪያዎች",
            'arif_volunteer': "💼 አሪፍ ፔይ በጎ ፈቃደኞች",
            'arif_intern': "🎓 አሪፍ ፔይ የ ስራ ልምምድ",
            'arif_jobs': "🔧 አሪፍ ፔይ ስራዎች",
            'Other_supports': "🛟 ሌሎች ድጋፎች"
        }

    buttons = []
    for key, text in options.items():
        if key == "arif_volunteer":
            url = 'https://arifpay.net/arif-volunteer'
        elif key == "arif_intern":
            url = 'https://arifpay.net/arif-intern'
        elif key == "arif_jobs":
            url = 'https://arifpay.net/jobs'
        elif key == 'Other_supports':
            url = 'https://t.me/iv?url=https://arifpay.net/support'
        else:
            url = None
        
        if url:
            buttons.append([InlineKeyboardButton(text, url=url)])
        else:
            buttons.append([InlineKeyboardButton(text, callback_data=key)])


    # Ensure buttons are grouped into 2 columns
    # buttons_in_rows = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
    buttons_in_rows = [row for row in buttons]
            
    # Create the InlineKeyboardMarkup
    reply_markup = InlineKeyboardMarkup(inline_keyboard=buttons_in_rows)

    # Send the message with the inline keyboard
    await context.bot.send_message(chat_id=chat_id, text="Please select an option:", reply_markup=reply_markup)

async def payment_issue_menu(chat_id: int, context: CallbackContext) -> None:
    """Display payment issue options based on the selected language."""
    language = context.user_data.get('language', 'language_en')
    if language == 'language_en':
        options = {
            'pos_support': "🏦 POS Support",
            'online_payment': "💻 Online Payment"
        }
    else:  # Amharic language
        options = {
            'pos_support': "🏦 የPOS ድጋፍ",
            'online_payment': "💻 የኦንላይን ክፍያ"
        }

    buttons = [
        [InlineKeyboardButton(options['pos_support'], callback_data='pos_support')],
        [InlineKeyboardButton(options['online_payment'], callback_data='online_payment')]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await context.bot.send_message(chat_id=chat_id, text="Please select an option:", reply_markup=reply_markup)

async def button(update: Update, context: CallbackContext) -> None:
    """Handle button callback queries."""
    query = update.callback_query
    await query.answer()

    # Handle button selection based on callback data
    if query.data == 'payment_issue':
        await payment_issue_menu(query.message.chat_id, context)
        
    
    language = context.user_data.get('language', 'language_en')  # Default to English if language is not set
    if query.data == 'how_to_guides':
        if language == 'language_en':
            response_text = (
                "📘 **How-to Guides** 📘\n\n"
                "1. **Using POS Machines**:\n"
                "   - Step 1: Turn on the POS machine.\n"
                "   - Step 2: Insert or swipe the customer's card.\n"
                "   - Step 3: Enter the amount to be charged.\n"
                "   - Step 4: Follow the prompts to complete the transaction.\n"
                "   ![Using POS Machines]\n\n"
                "2. **Online Payments**:\n"
                "   - Step 1: Visit our online payment portal.\n"
                "   - Step 2: Enter your payment details.\n"
                "   - Step 3: Confirm and complete the payment.\n"
                "   ![Online Payments]"
            )
            pos_gif_description = "Here is a demonstration of using POS machines:"
            online_payments_gif_description = "Here is a  demonstration of making online payments:"
        else:  # Amharic language
            response_text = (
                "📘 **አጠቃቀም እና መመሪያዎች** 📘\n\n"
                "1. **የPOS ማሽኖችን መጠቀም**:\n"
                "   - እርምጃ 1: የPOS ማሽኑን አብር.\n"
                "   - እርምጃ 2: የደንበኛውን ካርድ አስገባ ወይም ተንሸራተት.\n"
                "   - እርምጃ 3: ለማስፈጸም ያስፈለገውን መጠን አስገባ.\n"
                "   - እርምጃ 4: ሂደቱን ለመጨረስ መመሪያውን ተከተል.\n"
                "   ![የPOS ማሽኖችን መጠቀም]\n\n"
                "2. **ኦንላይን ክፍያዎች**:\n"
                "   - እርምጃ 1: ወደ እኛ የኦንላይን ክፍያ ገጽ ጎብኝ.\n"
                "   - እርምጃ 2: የክፍያውን ዝርዝሮች አስገባ.\n"
                "   - እርምጃ 3: እናም ክፍያውን አረጋግጥ.\n"
                "   ![ኦንላይን ክፍያዎች]"
            )
        pos_gif_description = "የPOS ማሽኖች አጠቃቀም ማሳያ:"
        online_payments_gif_description = 'የመስመር ላይ ክፍያዎችን የመፈጸም ማሳያ:'
    
    # await query.edit_message_text(text=response_text)
    await query.message.reply_text(response_text, parse_mode= 'Markdown')

    with open('./gif2.gif', 'rb') as pos_gif_file:
        await context.bot.send_message(chat_id= query.message.chat_id, text=pos_gif_description)
        await context.bot.send_animation(chat_id= query.message.chat_id, animation = pos_gif_file)
    with open('./gif3.gif', 'rb') as posOne_gif_file:
        await context.bot.send_message(chat_id= query.message.chat_id, text=online_payments_gif_description)
        await context.bot.send_animation(chat_id= query.message.chat_id, animation = posOne_gif_file)

async def cancel_command(update: Update, context: CallbackContext) -> None:
    """Cancel the current operation and return to the main menu."""
    await main_menu(update.effective_chat.id, context)

async def set_commands(application: Application) -> None:
    """Set the bot's commands for the menu button."""
    commands = [
        BotCommand(command="start", description="Start interacting with the bot"),
        BotCommand(command="cancel", description="Cancel the current operation and return to main menu")
    ]
    await application.bot.set_my_commands(commands)

def main() -> None:
    """Start the bot and register command and callback query handlers."""
    application = Application.builder().token(TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("cancel", cancel_command))

    # Register callback query handlers
    application.add_handler(CallbackQueryHandler(language_selected, pattern='^language_'))
    application.add_handler(CallbackQueryHandler(button))

    # Set the bot's commands for the menu button
    application.job_queue.run_once(set_commands, 0)

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()