import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShortChannelsComponent } from './short-channels.component';

describe('ShortChannelsComponent', () => {
  let component: ShortChannelsComponent;
  let fixture: ComponentFixture<ShortChannelsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShortChannelsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShortChannelsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
