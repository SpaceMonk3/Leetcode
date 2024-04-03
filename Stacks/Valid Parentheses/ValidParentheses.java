class Solution {
    public boolean isValid(String s) {
        Stack<Character> check = new Stack<Character>();

        for(int i = 0; i < s.length(); i++){
            if( (s.charAt(i) == '(') || (s.charAt(i) == '[') || (s.charAt(i) == '{') ){
                check.push(s.charAt(i));
            }
            else{
                switch(s.charAt(i)){
                    case ')':
                        if(check.empty() || check.pop() != '('){
                            return false;
                        }
                        break;
                    case ']':
                        if(check.empty() || check.pop() != '['){
                            return false;
                        }
                        break;
                    case '}':
                        if(check.empty() || check.pop() != '{'){
                            return false;
                        }
                        break;
                    default: 
                        break;
                }
            }
        }

        return check.empty();
    }
}


// {][()([])]}
//{)([]}        {()[]}
//    |       |
//    |       |
//    |       |   
//    |       |   
//    |       | 
//  } |       | {