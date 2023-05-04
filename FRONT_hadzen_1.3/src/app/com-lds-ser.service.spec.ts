import { TestBed } from '@angular/core/testing';

import { ComLdsSerService } from './com-lds-ser.service';

describe('ComLdsSerService', () => {
  let service: ComLdsSerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ComLdsSerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
