from supabase import create_client

url = "https://ryjkyqdjsrmzupntbczg.supabase.co"
key = "sb_publishable_Ki2l6YNQOL_sUzl7trtFNQ_0cFgwkpY"

supabase = create_client(url, key)

response = supabase.table("dashboard_config").select("*").limit(1).execute()

print("Supabase ativo")
