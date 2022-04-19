import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HomefundComponent } from './homefund.component';

describe('HomefundComponent', () => {
  let component: HomefundComponent;
  let fixture: ComponentFixture<HomefundComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HomefundComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HomefundComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
