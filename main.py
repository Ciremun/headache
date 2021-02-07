if __name__ == '__main__':
    import os
    from os.path import join, dirname
    
    from dotenv import load_dotenv
    
    import src.config
    import src.server
    from src.client import client
    
    load_dotenv(join(dirname(__name__), '.env'))
    client.run(os.environ.get('DISCORD_TOKEN'), bot=src.config.bot)
