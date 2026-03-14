import pandas as pd
import random
import string

# number of rows
NUM_ROWS = 5000

# sample merchant names
merchant_names = [
    "Fresh Mart","City Bakers","Daily Needs","Green Grocery","Urban Foods",
    "Amazon Support","Flipkart Deals","Paytm Cashback","PhonePe Help",
    "Mega Electronics","Smart Fashion","Quick Recharge","Online Offer"
]

# upi handles
handles = ["ybl","okaxis","ibl","paytm","okicici","axl"]

# suspicious keywords
suspicious_words = ["refund","cashback","offer","reward","support","help"]

# trap amounts
trap_amounts = [1,9,49,99,199,499,999]

data = []

def random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

for i in range(NUM_ROWS):

    name = random.choice(merchant_names)

    # generate upi id
    base = random_string(random.randint(5,10))
    
    if random.random() < 0.3:
        base += str(random.randint(10,999))

    handle = random.choice(handles)
    upi_id = base + "@" + handle

    amount = random.randint(1,5000)

    # features
    digit_count = sum(c.isdigit() for c in upi_id)
    upi_length = len(upi_id)

    suspicious_keyword = 1 if any(word in name.lower() for word in suspicious_words) else 0

    brand_impersonation = 1 if any(x in name.lower() for x in ["amazon","flipkart","paytm","phonepe"]) else 0

    trap_amount = 1 if amount in trap_amounts else 0

    report_count = random.randint(0,15)

    is_blacklisted = random.choice([0,1]) if report_count > 8 else 0

    merchant_age_days = random.randint(1,1000)

    # fraud rule for labeling
    fraud_score = (
        suspicious_keyword*2 +
        brand_impersonation*2 +
        trap_amount +
        (digit_count > 3) +
        (report_count > 5) +
        is_blacklisted
    )

    is_fraud = 1 if fraud_score >= 3 else 0

    data.append([
        upi_id,name,amount,
        suspicious_keyword,digit_count,upi_length,handle,
        brand_impersonation,trap_amount,
        report_count,is_blacklisted,merchant_age_days,
        is_fraud
    ])

columns = [
    "upi_id","merchant_name","amount",
    "suspicious_keyword","digit_count","upi_length","handle",
    "brand_impersonation","trap_amount",
    "report_count","is_blacklisted","merchant_age_days",
    "is_fraud"
]

df = pd.DataFrame(data,columns=columns)

df.to_csv("dataset.csv",index=False)

print("Dataset generated successfully!")
print(df.head())