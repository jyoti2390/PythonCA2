import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MyinvestmentComponent } from './myinvestment.component';

describe('MyinvestmentComponent', () => {
  let component: MyinvestmentComponent;
  let fixture: ComponentFixture<MyinvestmentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MyinvestmentComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MyinvestmentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
