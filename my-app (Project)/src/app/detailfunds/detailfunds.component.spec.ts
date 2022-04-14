import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DetailfundsComponent } from './detailfunds.component';

describe('DetailfundsComponent', () => {
  let component: DetailfundsComponent;
  let fixture: ComponentFixture<DetailfundsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DetailfundsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DetailfundsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
