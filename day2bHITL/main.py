import asyncio
from dotenv import load_dotenv
from google.adk.runners import InMemoryRunner
from agent import shipping_app # import code from agent.py

load_dotenv() # load API keys and settings
# Set a Runner using the imported application object
runner = InMemoryRunner(app=shipping_app)

async def main():
    session_id = "debug_session_id"
    
    print("\n🚀 Shipping Agent Ready! Type 'exit' or 'quit' to end the conversation.\n")
    
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            # Check if user wants to exit
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("\n👋 Goodbye!")
                break
            
            # Skip empty inputs
            if not user_input:
                continue
            
            # Send message to agent
            response = await runner.run_debug(
                user_input,
                session_id=session_id
            )
            
            print()  # Add spacing for readability

        except KeyboardInterrupt:
            print("\n\n👋 Conversation interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}\n")

if __name__ == "__main__":
    asyncio.run(main())