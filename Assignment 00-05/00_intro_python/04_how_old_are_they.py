def age_riddle():
    anton:int=21
    beth:int=anton+6
    chen:int = beth + 20
    drew:int = chen + anton
    ethan = chen
    print(f"Anton is {anton}")
    print(f"Beth is {beth}")
    print(f"Chen is {chen}")
    print(f"Drew is {drew}")
    print(f"Ethan is {ethan}")

if __name__=="__main__":
    age_riddle()