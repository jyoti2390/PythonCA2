import { Router } from '@angular/router';
import { AuthService } from './../services/auth.service';
import { FundService } from './../services/fund.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-homefund',
  templateUrl: './homefund.component.html',
  styleUrls: ['./homefund.component.css']
})
export class HomefundComponent implements OnInit {

  constructor(public fundService : FundService, public auth:AuthService, public router:Router) { }

  findByAmc(fundAmc: string){
    this.fundService.getAllByFundAmc(fundAmc);
  }

  ngOnInit(): void {
    this.fundService.getFunds();
    this.fundService.getFundAmc();
  }

  isSignin(){
    if (!this.auth.currentUser || this.auth.currentUser.userEmail == ''){
      this.router.navigateByUrl('/signin');
    }
    else{
      this.router.navigateByUrl('/funds')
    }
       
  }

  searchFund(name:string) {
    this.fundService.getAllByFundAmc(name);
    name = ''
    if (this.router.url !== 'funds') {
      this.fundService.searchFlag = true
      this.router.navigateByUrl('/funds');
    }

  }

}
