#pragma once

#include <assert.h>
#include <stdlib.h>

#include "mytypes.h"

template <class T>
class Array {
  T* elems;
  u32 num_elems;
  u32 used_elems;

public:
  Array(u32 size = 10) {
    elems = (T*)malloc(sizeof(T) * size);
    num_elems = size;
    used_elems = 0;
  }

  ~Array() {
    if (elems) free(elems);
    elems = nullptr;
  }

  T* begin() { return &elems[0]; }

  T* end() { return &elems[used_elems]; }

  const T* begin() const { return &elems[0]; }

  const T* end() const { return &elems[used_elems]; }

  T& operator[](u32 index) {
    assert(index < used_elems);
    return elems[index];
  }
  const T& operator[](u32 index) const {
    assert(index < used_elems);
    return elems[index];
  }

  u32 push_back(T elem) {
    if (used_elems + 1 >= num_elems) {
      resize(num_elems * 2);
    }
    elems[used_elems++] = elem;
    return used_elems - 1;
  }

  void resize(u32 new_size) {
    if (new_size < num_elems) return;
    elems = (T*)realloc(elems, sizeof(T) * new_size);
    assert(elems != nullptr);
    num_elems = new_size;
  }
  u32 size() const { return used_elems; }
  void reset() { used_elems = 0; }
  void reset(u32 new_used) {
    assert(new_used <= used_elems);
    used_elems = new_used;
  }
  u32 total_size() const { return num_elems; }

  T& getNextFree() { return elems[used_elems++]; }
};
