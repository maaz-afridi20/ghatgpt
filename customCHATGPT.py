import streamlit as st
import openai as ai
import requests

# ai.api_key = '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'


# def BasicGeneration(userPrompt):
#     completion = ai.ChatCompletion.create(
#         model = "gpt-3.5-turbo",
#         messages = [
#             {"role":"user","content":userPrompt}
#         ]
#     )
#     return completion.choices[0].message.content


# prompt = 'explain what is python'

# response = BasicGeneration(prompt)

# print(response)

# # #



url = "https://coinranking1.p.rapidapi.com/coins"

querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h","tiers[0]":"1","orderBy":"marketCap","orderDirection":"desc","limit":"50","offset":"0"}

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

#