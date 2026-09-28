import os
from supabase import create_client

url = os.environ["SUPABASE_URL"].strip()
key = os.environ["SUPABASE_KEY"].strip()

supabase = create_client(url, key)
response = supabase.table("dashboard_config").select("*").limit(1).execute()
print("OK:", response.data)
