export class User {
    userId: number;
    userName: string;
    userPassword: string;
    userEmail: string;
    userPhoneNumber:String;
    userAge:String;
    imgSrc: String;
  
    constructor() {
      this.userId = 0;
      this.userName = '';
      this.userEmail = '';
      this.userPassword = '';
      this.userPhoneNumber='';
      this.userAge='';
      this.imgSrc='';
    }
  }