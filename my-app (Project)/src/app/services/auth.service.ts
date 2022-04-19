import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { User } from '../model/user';
import { HttpHeaders } from '@angular/common/http';


@Injectable({
  providedIn: 'root',
})
export class AuthService {
  currentUser: User;
  constructor(public http: HttpClient) {
    this.currentUser = new User();
  }

  

  signUp(user: any) {
      const httpOptions = {
        headers: new HttpHeaders({
          'Authorization': 'Basic ' + btoa('user:admin')
        })
      };
    return this.http.post<User>('http://52.176.47.148:8080/user/add', user,httpOptions);
  }

  signIn(user: any) {
    const httpOptions = {
      headers: new HttpHeaders({
        'Authorization': 'Basic ' + btoa('user:admin')
      })
    };
    return this.http.post<User>('http://52.176.47.148:8080/signin', user,httpOptions);
  }
}