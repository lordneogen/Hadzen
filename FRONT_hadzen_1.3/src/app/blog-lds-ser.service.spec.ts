import { TestBed } from '@angular/core/testing';

import { BlogLdsSerService } from './blog-lds-ser.service';

describe('BlogLdsSerService', () => {
  let service: BlogLdsSerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(BlogLdsSerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
