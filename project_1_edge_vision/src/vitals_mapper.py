from datetime import datetime


class GeriatricMapper:
    def process(self, raw):
        nums = sorted(raw["numbers"], reverse=True)
        keys = raw["keywords"]
        packet = {"timestamp": datetime.now().isoformat()}

        # 1. BP
        if len(nums) >= 2 and (nums[0] > 60 and nums[1] > 30):
            packet["blood_pressure"] = {"sys": nums[0], "dia": nums[1]}
            nums = nums[2:]

        # 2. Temp (Specific Float Range)
        for n in nums[:]:
            if 34.0 <= n <= 42.0:
                packet["temp"] = {"value": n}
                nums.remove(n)
                break

        # 3. SpO2 & Pulse
        for n in nums[:]:
            if 90 <= n <= 100 and "spo2" not in packet:
                packet["spo2"] = {"value": n}
                nums.remove(n)
            elif 40 <= n <= 140 and "pulse" not in packet:
                packet["pulse"] = {"value": n}
                nums.remove(n)

        # 4. RR & MMSE (Small integers, keyword dependent)
        for n in nums[:]:
            if "RR" in keys or (10 <= n <= 30 and "respiration_rate" not in packet):
                packet["respiration_rate"] = {"value": n}
                nums.remove(n)
            elif "MMSE" in keys and n <= 30:
                packet["mmse"] = {"score": n}
                nums.remove(n)

        # 5. Glucose (Uses remaining float/int)
        for n in nums[:]:
            if 2.0 <= n <= 30.0:
                packet["glucose"] = {"value": n, "unit": "mmol/L"}
                nums.remove(n)
                break

        # 6. Elimination (Keyword Driven)
        if "ML" in keys:
            packet["urine_output"] = {"value": max(nums) if nums else 0}

        if "BM" in keys or "DAYS" in keys:
            # We assume a small number representing 'Days Since'
            packet["bowel_movement"] = {"days_since": min(nums) if nums else 0}

        return packet
