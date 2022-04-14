  
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { User } from '../model/user';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-sign-in',
  templateUrl: './sign-in.component.html',
  styleUrls: ['./sign-in.component.css'],
})
export class SignInComponent implements OnInit {
  user: User;
  successFlag: boolean;
  errorFlag: boolean;
  emailError:boolean;
  
  constructor(public auth: AuthService, public router: Router) {
    this.user = new User();
    this.successFlag = false;
    this.errorFlag = false;
    this.emailError=false;
  }
  ngOnInit(): void {}

  // isHome(){
  //   return this.router.url.includes("");
  // }

  signInSubmit(signInForm: any) {
    this.successFlag = false;
    this.errorFlag = false;
    console.log("hello")

    this.auth.signIn(this.user).subscribe(
      (res) => {
        console.log(res + "abc");
        if (res) {
          this.user = new User();
          signInForm.form.markAsPristine();
          this.auth.currentUser = res;
          this.successFlag = true;
          console.log(res.userName)
        } else {
          this.errorFlag = true;
        }
      },
      (error) => {
        this.errorFlag = true;
      }
    );
  }

  signUpSubmit(signUpForm: any) {
    this.successFlag = false;
    this.errorFlag = false;

    this.auth.signUp(this.user).subscribe(
      (res) => {
        console.log(res);
        if (res.userId != 0) {
          this.user = new User();
          signUpForm.form.markAsPristine();
          this.successFlag = true;
        } else {
          this.errorFlag = true;
        }
      },
      (error) => {
        // this.errorFlag = true;
        if(error.status==500){
          this.errorFlag=true;
          this.emailError=true;
        }
      }
    );
  }
}