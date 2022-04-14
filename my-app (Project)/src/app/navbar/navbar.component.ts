import { ActivatedRoute, Router } from '@angular/router';
import { Fund } from './../model/fund';
import { FundService } from './../services/fund.service';
import { Component, OnInit } from '@angular/core';
import { AuthService } from '../services/auth.service';
import { User } from '../model/user';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  userName: string;
  fund: Fund;
  fundId: number;
  fundName:string;
  constructor(public auth: AuthService, public fundService: FundService, public router: Router, public ar: ActivatedRoute) {
    this.userName = '';
    this.fund = new Fund;
    this.fundId = 0;
    this.fundName=''
  }

  ngOnInit(): void {
    this.fundService.getFunds();
  }

  navauth() {
    if (this.auth.currentUser.userEmail == '') {
      return true
    }
    else {
      return false
    }
  }

  loggedOut() {
    this.auth.currentUser = new User;
  }

  searchFund(name: string) {
    this.fundService.searchByName(name);
    this.fundName = ''
    if (this.router.url !== 'funds') {
      this.fundService.searchFlag = true
      this.router.navigateByUrl('/funds');
    }

  }
}
