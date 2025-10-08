from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="api-key",
)
command = '''
[4:13 pm, 6/10/2025] DC: Kuch na soke utha tha tu bata
[4:48 pm, 6/10/2025] Arpit Saxena: Bs dekh r movie dekh ra hu
[5:20 pm, 6/10/2025] DC: Bhej link jldi
[12:13 pm, 7/10/2025] DC: Next week ka bata kab chuti hogi teri ?
[12:15 pm, 7/10/2025] Arpit Saxena: safe side k liye tuesday maan le
[12:17 pm, 7/10/2025] DC: Acha aur Diwali ki kitto chutii?
[12:18 pm, 7/10/2025] Arpit Saxena: 17 se 23
[12:18 pm, 7/10/2025] DC: Ghar kab jaega ?
[12:19 pm, 7/10/2025] Arpit Saxena: 17 ko
[4:36 pm, 7/10/2025] Arpit Saxena: Ky kr rh
[4:38 pm, 7/10/2025] DC: Kuch na call le raha
'''

completion = client.chat.completions.create(
  model="openai/gpt-oss-20b:free",
  messages=[
    {
      "role": "user",
      "content": command
    }
  ]
)
print(completion.choices[0].message.content)