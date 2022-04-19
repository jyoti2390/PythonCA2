import { UserFund } from './../model/userfund';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { HttpHeaders } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class UserfundService {
  userFund: UserFund[];
  userFundHistory:any
  userId: number;
  totalFund: number;

  constructor(public http: HttpClient) {
    this.userFund = [];
    this.userId = 0;
    this.totalFund=0;
  }

  getFundHistoryByUserId(userId: number) {
    this.http.get<UserFund[]>('http://52.176.47.148:8080/fundsHistoryById/' + userId).subscribe((res) => {
      this.userFundHistory = res;
    });
  }

  addUserFund(userFund: any) {
    const httpOptions = {
      headers: new HttpHeaders({
        'Authorization': 'Basic ' + btoa('user:admin')
      })
    };
    return this.http.post<UserFund>('http://52.176.47.148:8080/userfund/add', userFund,httpOptions);
  }

  findTotalFund(id:number){
    return this.http.get<number>('http://52.176.47.148:8080/fundtotal/' + id).subscribe((res)=>{
    this.totalFund = res;
    console.log(res)
    });
  }
}
