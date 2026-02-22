import sqlite3
import pandas as pd
import random

data = {
    'id': range(1, 51),
    'product_name': [
        'Python Course', 'Java Masterclass', 'Data Science Bootcamp', 
        'React Native Guide', 'Advanced Excel', 'Machine Learning A-Z',
        'Web Dev Complete', 'Figma UI/UX', 'Docker for Beginners',
        'Kubernetes Deep Dive', 'SQL for Data Analysis', 'PowerBI Pro',
        'Tableau Visualization', 'Android Dev with Kotlin', 'iOS with Swift',
        'Cybersecurity Basics', 'Ethical Hacking', 'Cloud Computing AWS',
        'Azure Fundamentals', 'Google Cloud Architect', 'DevOps Lifecycle',
        'Linux Command Line', 'Bash Scripting', 'C++ Game Dev',
        'Unity 3D', 'Unreal Engine 5', 'Blender 3D Modeling',
        'Digital Marketing', 'SEO Strategies', 'Content Writing',
        'Copywriting 101', 'Social Media Manager', 'Facebook Ads',
        'Google Ads Expert', 'Affiliate Marketing', 'Email Marketing',
        'Dropshipping 2024', 'E-commerce Business', 'Shopify Master',
        'Accounting Basics', 'Finance for Non-Finance', 'Stock Trading',
        'Crypto Investing', 'Blockchain Theory', 'NFT Creation',
        'Smart Contracts Solidity', 'Gen AI with LLMs', 'Prompt Engineering',
        'LangChain Agents', 'Computer Vision'
    ],
    'category': ['Programming', 'Design', 'Marketing', 'Business', 'Finance'] * 10,
    'price': [random.randint(10, 200) for _ in range(50)]
}

df=pd.DataFrame(data)

conn=sqlite3.connect('inventory.db')
df.to_sql('products',conn,if_exists='replace',index=False)

print("Done")