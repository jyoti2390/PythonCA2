import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-myprofile',
  templateUrl: './myprofile.component.html',
  styleUrls: ['./myprofile.component.css']
})
export class MyprofileComponent implements OnInit {

  constructor(public auth: AuthService, public router:Router) { }

  ngOnInit(): void {
    if (!this.auth.currentUser || this.auth.currentUser.userEmail == '')
       this.router.navigateByUrl('/signin');
  }

}
