import { UserFund } from './../model/userfund';
import { UserfundService } from './../services/userfund.service';
import { Router } from '@angular/router';
import { AuthService } from './../services/auth.service';
import { Component, OnInit } from '@angular/core';
import { FundService } from '../services/fund.service';

@Component({
  selector: 'app-buy',
  templateUrl: './buy.component.html',
  styleUrls: ['./buy.component.css']
})
export class BuyComponent implements OnInit {
  
  successFlag: boolean;
  userFund:UserFund;


  date : string = new Date().toDateString();

  constructor(public fundService: FundService , public auth: AuthService,
     public router:Router, public userFundService: UserfundService) {
       this.userFund = new UserFund;
       this.successFlag = false;
      }

  ngOnInit(): void {
    if (!this.auth.currentUser || this.auth.currentUser.userEmail == '')
       this.router.navigateByUrl('/signin');
  }

  addUserFund(isValue:any){
    this.successFlag = false;
    this.userFund.userId = this.auth.currentUser.userId;
    this.userFund.ufDate = this.date;
    this.userFund.fundId = this.fundService.fundDetails[0][12];
    this.userFund.ufType = this.fundService.fundDetails[0][4];
    // console.log(this.userFund)
    this.userFundService.addUserFund(this.userFund).subscribe(
      (res)=>{
        if(res){
          this.userFund = new UserFund();
          this.successFlag = true;
          isValue.form.markAsPristine();
        }
        

        console.log(res);
      }
    )
  }

}
