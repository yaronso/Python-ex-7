import sys
import os
"""
*Student name: Yaron Sofer
*Student ID: 313293532
*Exercise name: ex7
"""

def insert_file_to_dictionary():
    """
    Explanation about what the function does
    -the function reading from the input.txt to a dictionary
    -the dictionary is a data base which contain all the actors and the movies.
    Keyword Arguments: none
    Return: the new dictionary call 'movies'
    """
    file = open(sys.argv[1], "r")
    #movies is my the dictionary
    movies = {}
    for line in file:
        read = line.strip().split(', ')
        for i in range(1, len(read)):
            if  not read[i] in movies:
                movies[read[i]] = {read[0]}
            else:
                movies[read[i]].add(read[0])
    return movies

#calling the function
movies = insert_file_to_dictionary()


def option1(movies):
     """
    Explanation about what the function does
    - the user input two movies and an operator and the function
    -checks 3 diffrent cases about the actors in each movie
    Keyword Arguments: movies - the dictionary
    Return: none, just print
    """
    #input to the varaible twoMovies
     twoMovies = input("Please select two movies and an operator(&,|,^) separated with ',':\n")
     twoMovies = twoMovies.split(',')
     #the loop cleans the spaces
     for i in range(len(twoMovies)):
            twoMovies[i] = twoMovies[i].strip()
     #in a case the input isn't exist in the dictionary
     if twoMovies[0] not in movies.keys() or twoMovies[1] not in movies.keys() or twoMovies[2] not in {'&','|','^'}:
         print('Error')
         return
     movie1 = twoMovies[0]
     movie2 = twoMovies[1]
     operator = twoMovies[2]
     if operator == '&':
            players1 = set(movies[movie1])
            players2 = set(movies[movie2])
            together = players1&players2
            # sorting according the 'abc serial
            together = sorted(together)
            #if there are no actors in the following group
            if not together:
                print("There are no actors in this group")
            else:
                print (', '.join(together))
     if operator == '|':
            players1 = set(movies[movie1])
            players2 = set(movies[movie2])
            together = players1|players2
            #sorting according the 'abc serial
            together = sorted(together)
            # if there are no actors in the following group
            if not together:
                print("There are no actors in this group")
            else:
                print (', '.join(together))
     if operator == '^':
             players1 = set(movies[movie1])
             players2 = set(movies[movie2])
             together = players1^players2
             # sorting according the 'abc serial
             together = sorted(together)
             # if there are no actors in the following group
             if not together:
                 print("There are no actors in this group")
             else:
                 print(', '.join(together))

def option2(movies):
     """
       Explanation about what the function does
       - the user input a name of an actor and the function
       - check all the other actors which played with him in random movie
       - they are also cases when the actor isn't in the data base
       Keyword Arguments: movies - the dictionary
        Return: none, just print
       """
     playerName = input ('Please select an actor:\n')
     flag = 0
     for k in movies.keys():
       #if the player is in the dictionary's keys
       if playerName in movies[k]:
           flag = 1
     if flag == 0:
         print("Error")
         return
     otherPlayers = []
     otherPlayers = set(otherPlayers)
     for x in movies.keys():
        #the condition verify if the actor is one of the values
        if playerName in movies[x]:
            otherPlayers = set(otherPlayers | movies[x])
     otherPlayers.remove(playerName)
     #sorting according the 'abc' serial
     otherPlayers = sorted(otherPlayers)
     #if they are no actors in the group
     if not otherPlayers:
         print("There are no actors in this group\n")
         return 
     print(', '.join(otherPlayers)) 
     return

def option3(movies):
         """
           Explanation about what the function does
           - the user input a name of a new movie or have to update
           - if the movie exists but they are new actors so the
           - function updates the dictionary
           Keyword Arguments: movies - the dictionary
            Return: none, just prints if there is a error
           """
         newMovie = input('Please insert a new movie:\n')
         newMovie = newMovie.split(',')
         #the following loop clean the spaces
         for i in range(len(newMovie)):
              newMovie[i] = newMovie[i].strip()
         #verify if the input is valid
         if (len(newMovie) < 2):
              print('Error')
              return
         #if the movie exists
         if newMovie[0] in movies.keys():
             #the first location in the input
             movieName = newMovie[0]
             movies[newMovie[0]] = movies[newMovie[0]] | set(newMovie[1:])
         else:
             movies[newMovie[0]] =  set(newMovie[1:])
         return



def option4(movies):
        """
              Explanation about what the function does
              - The function write the data to the output file and print it
              Keyword Arguments: movies - the dictionary (the data base)
              Return: none, just prints the information to the output file
              """
        #recieving the output file by a command line
        file_outPut = sys.argv[2]
        os.chmod(file_outPut, 0o777)
        file_outPut = open(file_outPut, "w")
        #creating a list for all the actors from my dictionary
        actorList =  (movies.values())
        newActors = set()
        for s in actorList:
            newActors = newActors|s
        newActors = sorted(newActors)
        #creating a list for all the movies from my dictionary
        movieList = sorted (movies.keys())
        #iterating on the actors list
        for actor in newActors:
            temp = []
            #iterating over the movies list
            for movie in movieList:
                if actor in movies[movie]:
                    #adding to temp all the movies which the actor act in them
                    temp.append(movie)
            #print to a file
            temp = [actor] + temp
            file_outPut.write(', '.join(temp))
            file_outPut.write('\r\n')
        #close the file
        file_outPut.close()


def start():
    """
    Explanation about what the function does
     ask the user to select an option as an input
     Keyword Arguments: none
     Return: the option that the user chose
    """
    print("Please select an option:")
    print("1) Query by movies")
    print("2) Query by actor")
    print("3) Insert a new movie")
    print("4) Save and Exit")
    print("5) Exit")
    option = input()
    return option


def main():
    """
    Explanation about what the function does
    The function get the value of the option that the user already chose
    in the function called 'start' and calls the compatible function according
    the option's value.
    Keyword Arguments: none
    Return: none
    """
    print('Processing...')
    option = start()
    while (option in ('1', '2', '3')):
        if option == '1':
            option1(movies)
        if option == '2':
            option2(movies)
        if option == '3':
            option3(movies)
        option = start()
    #outside the loop
    if option == '4':
        option4(movies)
        return
    if option == '5':
        return

main()
