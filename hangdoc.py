import pandas as pd
import random
import os

def main():
    random.seed()

    df = pd.read_csv("data.csv", dtype=str)

    keywords = df['Keyword'].dropna().values.tolist()

    keywords = list(set(keywords))

    keywords = ["".join(s.split()).upper() for s in keywords]

    keywords = [word for word in keywords if len(word) in range(10, 17)]

    df = pd.DataFrame({'Keyword': keywords})

    df.to_csv("data.csv", index=False)
    
    print("Number of keywords: ", len(keywords))

    while True:
        word = random.choice(keywords)
        
        n = len(word)
        
        hidden_positions = list(range(len(word)))
        
        while True:
            os.system("cls")
            for i in range(n):
                print(str(i + 1).rjust(3, ' '), end='')
            print()
            for i in range(n):
                if i in hidden_positions:
                    print('_'.rjust(3, ' '), end='')
                else:
                    print(word[i].rjust(3, ' '), end='')
            print()
            
            user_input = input()
            if user_input in ['QUIT', 'q', 'Q']:
                print(word)
                return
            elif user_input in ['HINT', 'h', 'H', '']:
                idx = random.choice(hidden_positions)
                hidden_positions.remove(idx)
            elif user_input in ['NEXT', 'n', 'N']:
                break
            elif user_input == word:
                print('Correct!')
                print('Press Enter to contiune!')
                _ = input()
                break
            else:
                print('Good luck next time!')


if __name__ == "__main__":
    main()