try:
    import pymongo
    from pymongo import *
    from pymongo.errors import *
    from clonerdb import *

    

    async def update_mongodb(bot_username, new_mongodb):
        data = {"bot_username": bot_username}
        new_value = {"$set": {"mongodb": new_mongodb}}
        try:
            result = cloned_tokens_collection.update_one(data, new_value)
        except Exception as e:
            print(f"Error updating MongoDB: {str(e)}")

    async def update_fsub(dk, new_db):
        data = {"bot_username": dk}
        new_value = {"$set": {"fsub": new_db}}
        try:
            result = cloned_tokens_collection.update_one(data, new_value)
        except Exception as e:
            print(f"Error updating fsub: {str(e)}")

    async def update_help_msg(dk, new_db):
        data = {"bot_username": dk}
        new_value = {"$set": {"help_msg": new_db}}
        try:
            result = cloned_tokens_collection.update_one(data, new_value)
        except Exception as e:
            print(f"Error updating help_msg: {str(e)}")

    async def update_start_msg(dk, new_db):
        data = {"bot_username": dk}
        new_value = {"$set": {"start_msg": new_db}}
        try:
            result = cloned_tokens_collection.update_one(data, new_value)
        except Exception as e:
            print(f"Error updating start_msg: {str(e)}")

    async def update_log_channel(dk, new_db):
        data = {"bot_username": dk}
        new_value = {"$set": {"log_channel": new_db}}
        try:
            result = cloned_tokens_collection.update_one(data, new_value)
        except Exception as e:
            print(f"Error updating log_channel: {str(e)}")

    async def update_bot_lang(dk, new_db):
        data = {"bot_username": dk}
        new_value = {"$set": {"bot_lang": new_db}}
        try:
            result = cloned_tokens_collection.update_one(data, new_value)
        except Exception as e:
            print(f"Error updating bot_lang: {str(e)}")

    async def update_font(dk, new_db):
        data = {"bot_username": dk}
        new_value = {"$set": {"font": new_db}}
        try:
            result = cloned_tokens_collection.update_one(data, new_value)
        except Exception as e:
            print(f"Error updating font: {str(e)}")

    async def update_button_link(dk, new_db):
        data = {"bot_username": dk}
        new_value = {"$set": {"button_link": new_db}}
        try:
            result = cloned_tokens_collection.update_one(data, new_value)
        except Exception as e:
            print(f"Error updating button_link: {str(e)}")

    async def update_privatepass(dk, new_db):
        data = {"bot_username": dk}
        new_value = {"$set": {"privatepass": new_db}}
        try:
            result = cloned_tokens_collection.update_one(data, new_value)
        except Exception as e:
            print(f"Error updating privatepass: {str(e)}")

except ImportError:
    # Handle the case where pymongo is not installed
    print("pymongo is not installed.")
except Exception as e:
    # Handle other exceptions
    print(f"An error occurred: {str(e)}")
