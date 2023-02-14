function makeUser(){
    return this; // this time there's no object literal
  }
  
  alert( makeUser().name );