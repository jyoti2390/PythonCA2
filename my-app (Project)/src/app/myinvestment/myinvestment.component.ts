import { Router } from '@angular/router';
import { UserfundService } from './../services/userfund.service';
import { Component, OnInit } from '@angular/core';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-myinvestment',
  templateUrl: './myinvestment.component.html',
  styleUrls: ['./myinvestment.component.css']
})
export class MyinvestmentComponent implements OnInit {
  constructor(public userFundService:UserfundService, public auth:AuthService, public router: Router) {   }

  ngOnInit(): void {
    if (!this.auth.currentUser || this.auth.currentUser.userEmail == ''){
       this.router.navigateByUrl('/signin');
    }
    this.userFundService.getFundHistoryByUserId(this.auth.currentUser.userId);
    this.userFundService.findTotalFund(this.auth.currentUser.userId);
  }

  getByUserId(){
    this.userFundService.getFundHistoryByUserId(this.auth.currentUser.userId);
  }

}
