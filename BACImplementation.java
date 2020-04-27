/*
* Andrew Lishchenko 500815035
* Average score 5.1-5.2 guesses per word
* Mostly random choosing (math.random)
* Starting with words with most(or least) common letter increased guess time, pure random was faster
*/

import java.util.*;


class BACImplementation implements BACPlayer{
  List<String> allPossibleWords = new ArrayList<String>();
  List<String> roundWords = new ArrayList<String>();

  public String getAuthor(){return("Lishchenko,Andrew");}
  
  public String getStudentID(){return("500815035");}

  public void initializeWordList(List<String> words){
    allPossibleWords=words;
  }
  
  public String guess(int n, List<String> guesses, List<Integer> bulls, List<Integer> cows){
    String attempt="";
    if(guesses.size()==0){//reduces list of possible words based of size and guesses random word at the start
      roundWords=setList(n);
      attempt = roundWords.get((int)(Math.random()*roundWords.size())); 
    }
    else{//every other guess after the first
      int num=guesses.size()-1;
      roundWords=editList(bulls.get(num),cows.get(num),guesses.get(num));
      attempt = roundWords.get((int)(Math.random()*roundWords.size())); 
    }
    return(attempt);
  }
  private List<String> setList(int n){
    List<String> answer = new ArrayList<String>();
    for(String a:allPossibleWords){
      if(a.length()==n){
        answer.add(a);
      }
    }
    return(answer);
  }
  
  private List<String> editList(int bulls, int cows, String guess){
    List<String> answer = new ArrayList<String>();
    int[] bc = {0,0};
    int len = guess.length();
    
    
    if(bulls==0 && cows==0){
      for(String a:roundWords){ // all words in the list
        int flag=0;

        for(int b=0;b<a.length();b++){ // all characters in the word in the list
          for(int c=0;c<len;c++){ //all characters in the guess word
            if(a.charAt(b)==guess.charAt(c)){
              flag++;
              break;
            }
            if(flag!=0)
              break;
          }
        }
        if(flag==0)
          answer.add(a);
      }
    }
    else{      
      for(String a:roundWords){// for every word in the available list
        countBullsAndCows(a,guess,bc);//check the pervious guess against all possible words
        if(bc[0]==bulls && bc[1]==cows)
          answer.add(a);
      }
    }
      return answer;
  }
  
  
  private static void countBullsAndCows(String guess, String secret, int[] out) {
        boolean[] seen = new boolean[26];
        for(int i = 0; i < secret.length(); i++) {
            int c = ((int)secret.charAt(i)) - 'a';
            seen[c] = true;
        }
        int bulls = 0, cows = 0;
        try {
            for(int i = 0; i < secret.length(); i++) {
                int c1 = ((int)secret.charAt(i)) - 'a';
                int c2 = ((int)guess.charAt(i)) - 'a';
                if(c1 == c2) { bulls++; }
                else if(seen[c2]) { cows++; }
            }
        }
        catch(Exception e) { bulls = cows = 0; }
        out[0] = bulls; out[1] = cows;
    }
}