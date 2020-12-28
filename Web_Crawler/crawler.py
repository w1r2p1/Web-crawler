def extract_dates_from_file(file_content):
    sample = {'name': "fri 12",'index' : 5 }
    dates=[]
    for i , _byte in enumerate(file_content) :
        char =chr(_byte)
        if char == '*':
            break
        elif char == '<':
            prefix = file_content[i+1:i+37].decode('utf-8')
            i = i+38
            if prefix == 'div class="rcl-MarketHeaderLabel-isd' or prefix == 'div class="rcl-MarketHeaderLabel rcl':
                temp_date = ""
                i = i+27
                char = chr(file_content[i])
                i=i+1
                if char == 's':
                    i = i+8
                    char = chr(file_content[i])
                    i=i+1
                while not char == '<':
                    temp_date = temp_date + char
                    char = chr(file_content[i])
                    i=i+1
                dates.append({'data': temp_date,'index' : i })
            else:
                i=i+28
                i=i-63
    return dates

def extract_games_from_file(file_content,pattern ='div class="rcl-ParticipantFixtureDetails_Team "' ):
    games = []
    pattern_len = len(pattern)
    for i , _byte in enumerate(file_content) :
        char = chr(_byte)
        if char == '*':
            break
        elif char == '<':
            prefix = file_content[i+1:i+(pattern_len + 1)].decode('utf-8')
            i = i+(pattern_len + 1)
            if prefix == pattern:
                temp_team = ""
                char = chr(file_content[i])
                i=i+1
                if char == ' ':
                    i=i+9
                char = chr(file_content[i])
                i=i+1
                while not char == '<':
                    temp_team = temp_team + char
                    char = chr(file_content[i])
                    i=i+1
                games.append({'data' : temp_team, 'index' : i})
            else:
                i=i+17
                i=i-63
    return games
  

def extract_times_from_file(file_content,pattern ='div class="rcl-ParticipantFixtureDetails_BookCl' ):
    times = []
    pattern_len = len(pattern)
    for i , _byte in enumerate(file_content) :
        char = chr(_byte)
        if char == '*':
            break
        elif char == '<':
            prefix = file_content[i+1:i+(pattern_len + 1)].decode('utf-8')
            i = i+(pattern_len + 1)
            if prefix == pattern:
                temp_time = ""
                i=i+7
                char = chr(file_content[i])
                i=i+1
                while not char == '<':
                    temp_time = temp_time + char
                    char = chr(file_content[i])
                    i=i+1
                times.append({'data' : temp_time, 'index' : i})
            else:
                i=i+17  
                i=i-63
    return times

def extract_odds_from_file(file_content,pattern ='div class="rcl-MarketColumnHeader ">' ):
    indicator = 1
    home_odds = []
    guest_odds = []
    even_odds = []
    pattern_len = len(pattern)
    for i , _byte in enumerate(file_content) :
        char = chr(_byte)
        if char == '*':
            break
        elif char == '<':
            prefix = file_content[i+1:i+(pattern_len + 1)].decode('utf-8')
            i = i+(pattern_len + 1)
            if prefix == pattern:
                num = ""
                char = chr(file_content[i])
                i=i+1
                while not char == '<':
                    num = num + char
                    char = chr(file_content[i])
                    i=i+1
            elif prefix == 'span class="sgl-ParticipantOddsOnly8':
                i=i+8
                odd = ""
                char = chr(file_content[i])
                i=i+1
                while not char == '<':
                    odd = odd + char
                    char = chr(file_content[i])
                    i=i+1
                if num == "1":
                    home_odds.append(odd)
                elif num == "2":
                    guest_odds.append(odd)
                else:
                    even_odds.append(odd)
            else:
                i=i+28  
                i=i-63
    return [home_odds, guest_odds, even_odds]

#span class="sgl-ParticipantOddsOnly80_Odds">
#span class="sgl-ParticipantOddsOnly8
#div class="rcl-MarketColumnHeader ">
