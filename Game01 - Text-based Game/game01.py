# Text-based game about GRIMES
print('Are you a real fan of Grimes?')

ans = input('Are you a fan of Grimes? (yes/no): ')
score = 0
total_q = 7

if ans.lower() == 'yes':
    ans = input('1. What is her real nickname?: ')
    if ans.lower() == 'c':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')

    ans = input('2. When is Grimes birthday? (DD/MM/YYYY): ')
    if ans.lower() == '17/03/1988':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')

    ans = input('3. What is the latest song that Grimes released?: ')
    if ans.lower() == 'shinigami eyes':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')

    ans = input('4. What is the released date of Shinigami Eyes? (DD/MM/YYYY): ')
    if ans == '26/01/2022':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')

    ans = input('5. What is the best Grimes song of all time?: ')
    if ans.lower() == 'we appreciate power' or ans.lower() == 'entropy':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')

    ans = input('6. What is Grimes favorite meal ever?: ')
    if ans.lower() == 'spaghetti':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')

    ans = input('7. What did Grimes study in college?: ')
    if ans.lower() == 'neuroscience' or ans.lower() == 'the russian language' \
            or ans.lower() == 'neuroscience and the russian language':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')

    print('Are you actually a fan of Grimes!?, you got ', score, ' question(s) correct!')
    mark = (score/total_q) * 100

    print('Mark: ', str(mark) + '%')
    if score >= 5:
        print('Wow, you really a fan of her!')
    else:
        print('Sorry, maybe you are not her real fan, but I know that you love her!')

print('Goodbye then')
