import { Router } from '@angular/router';
import { AuthService } from './../services/auth.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {

  constructor(public auth: AuthService, public router: Router) { }

  ngOnInit(): void {
  }

  isSignin(){
    if (!this.auth.currentUser || this.auth.currentUser.userEmail == ''){
      this.router.navigateByUrl('/signin');
    }
    else{
      this.router.navigateByUrl('/myprofile')
    }
  }

}
