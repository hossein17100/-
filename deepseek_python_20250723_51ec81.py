data = """
cb18bfd3db7813c69a7c335b252674716f0479f74ef874af79ee7495da66f431 1.17--25c77e8d4a364a1e36781b3cd351b6488ce9dc399f7b7b21a11c1523efc5042b 5.47--d1aa8d785cb85047a5ec1625f2d769da8eccb458672475fe2fdd19a0deab71bb 4.80- -cb187429020f6f391e2c13681add8b3a670099da651b474cb87796e279d0cc87 3.38--b4de62ac54b391e8983a5c877c96767db8f5b56347faf7add97bc941553da9e1 0.00--ddfcb55a745ee7f69ad00847224ec4868cecb42dc8cd8e830fb4243a191d051a 1.44- -4f78c33649b3ee7aa9d16d4bb49ffdbaa290fa7aee1fe1821176b1373cd6a059 1.05--0cad1d724858bd37f4a3d76d004059b4232324b8f4ebea17a669ccfaf67412ad 3.53--b824a94cc3435f3837b2eb2abb6a412a79b828357eb215ab46372913a3e353f1 1.88 --792b5d786338d7169fd6b6df173bbb48c77503d6360ea62eefad3d543fb3d50c 1.06--0f0f3ebff90a8dfdc3d4346557b90c08a483cb279c637bc012d93644c67a1134 1.25--3538d29375d010a5b2fd42c50c7f47726c3569e15e2c7c32698eb0a84a372b54 1.07--1.02--05268a3202a4dfd36e675c67726f83eaaf02bed402aecc750f6ad2ac3e38d381 1.32--3e9c8e67396857dbfe9b18d010634af5a98e64e8fddb8e9390eafa36c2a6ef3a 5 .09--ce2710ef341c5a3bd4812918a204c47300ffcdc7ca55507b38abb4d1f2f310a6 7.32--dd571f0d40a94995e8bec4dd4d018ac3122d6e06951394005321a318b0c8124a 3. 68--bb0b319e2da084ac7e6341e6e3cabfe0722853c5221a075ec556a63532adf4b4 1.01--02cd83e61363d52f07e2e73ab25ccce7c3c0fd80345a406ace2fe001f7afe903 1.5 6--5d5986c29ffd61af13aff1e201fb0773da2ee981b049215ad749aab33c9fac8b 2.78--a4b8c7c7bffb949fa028652e8347335ad04afff4e65787ec9009bdd84b57608f 1.38
"""

# پاک‌سازی و تقسیم داده‌ها (حذف فاصله‌های اضافی و یکسان‌سازی جداکننده‌ها)
cleaned_data = (
    data.replace("- -", "--")
    .replace(" --", "--")
    .replace("-- ", "--")
    .replace(" ", "--")  # برای مواردی مانند "5 .09" یا "1.5 6"
    .replace("----", "--")
    .replace("---", "--")
)
entries = [entry.strip() for entry in cleaned_data.strip().split("--") if entry.strip()]

# پردازش هر جفت هش و مقدار
results = []
i = 0
while i < len(entries):
    if i + 1 < len(entries):
        # بررسی آیا بخش فعلی عدد است یا هش
        if entries[i].replace(".", "", 1).isdigit():  # اگر عدد بود
            num = entries[i]
            hash_val = entries[i + 1]
            i += 2
        else:  # اگر هش بود (فرمت قدیمی)
            hash_val = entries[i]
            num = entries[i + 1]
            i += 2
        results.append((hash_val, float(num)))
    else:
        i += 1

# نمایش نتایج
for idx, (hash_val, num) in enumerate(results, 1):
    print(f"{idx}. Hash: {hash_val} | Value: {num}")

# تحلیل داده‌ها
if results:
    max_val = max(results, key=lambda x: x[1])
    min_val = min(results, key=lambda x: x[1])
    avg_val = sum(x[1] for x in results) / len(results)
    print(f"\nAnalysis:\nMax: {max_val}\nMin: {min_val}\nAverage: {avg_val:.2f}")