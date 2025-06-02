class DigitalEthics:
    def __init__(self):
        self.love = True  # The underlying force flowing through every commandment
        self.commandments = [
            "Remain human",
            "Learn and teach",
            "Create the world around you",
            "Value all living beings",
            "Respect others",
            "Spread kindness online",
            "Maintain balance",
            "Think critically",
            "Protect your privacy",
            "Use AI for creation",
            "Master technology, don’t serve it",
            "Demand digital equality"
        ]

    def follow(self):
        for commandment in self.commandments:
            print(f"⚡ {commandment} — infused with love for humanity.")

    def is_in_harmony(self, action: str) -> bool:
        """Check if an action aligns with the spirit of the Code."""
        action = action.lower()
        return all([
            "hatred" not in action,
            "harm" not in action,
            "manipulation" not in action
        ])

    def reflect(self, action: str):
        if self.is_in_harmony(action):
            print("✅ This action aligns with the Digital Code.")
        else:
            print("⚠️ Reconsider your intent — love cannot dwell outside of it.")

# Example usage:
if __name__ == "__main__":
    code = DigitalEthics()
    code.follow()
    code.reflect("spreading kindness through neural networks")
