import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NewChanellComponent } from './new-chanell.component';

describe('NewChanellComponent', () => {
  let component: NewChanellComponent;
  let fixture: ComponentFixture<NewChanellComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NewChanellComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NewChanellComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
