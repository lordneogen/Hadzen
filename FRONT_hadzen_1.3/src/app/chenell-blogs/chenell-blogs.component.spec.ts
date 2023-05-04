import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChenellBlogsComponent } from './chenell-blogs.component';

describe('ChenellBlogsComponent', () => {
  let component: ChenellBlogsComponent;
  let fixture: ComponentFixture<ChenellBlogsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ChenellBlogsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ChenellBlogsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
