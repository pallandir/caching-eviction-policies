<a name="readme-top"></a>

<br />
<div align="center">
<a href="">
    <img src="assets/readme.svg" alt="Logo" width="80" height="80">
  </a>
  <h3 align="center">Common caching algorithms</h3>

  <p align="center">
    Learn about common caching algorithms and cache eviction policies
    <br />
    <br />
    <a href="https://github.com/pallandir/caching-eviction-policies/issues">Report Bug</a>
    ·
    <a href="https://github.com/pallandir/caching-eviction-policies/issues">Request Feature</a>
  </p>
</div>

## About this project

Caches are small memory units designed to store the most recently accessed data for a specific service. The limited memory capacity is primarily due to the high cost of components, such as RAM, used for data storage. To maintain consistent and useful data, various algorithms manage the data lifecycle, and cache eviction policies determine how data is refreshed. This project will explore the most common cache eviction algorithms.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUMMARY -->

## Summary

| Strategy                    | Eviction Policy                       | Best Use Case                                    |
| --------------------------- | ------------------------------------- | ------------------------------------------------ |
| First-In/First-Out (FIFO)   | Removes the oldest entry first        | When newer data is more relevant than older data |
| Last-In/First-Out (LIFO)    | Removes the most recent entry first   | When older data is more relevant than newer data |
| Least Recently Used (LRU)   | Removes the least recently used entry | When frequently accessed data should be kept     |
| Most Recently Used (MRU)    | Removes the most recently used entry  | When older data is more valuable than new data   |
| Least Frequently Used (LFU) | Removes the least accessed entry      | When popular data should be prioritized          |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTENT -->

## Content

1.  [FIFO caching](FIFO.md)
2.  [LRU caching]()
3.  [LFU caching]()
4.  [LIFO caching]()
5.  [MRU caching]()

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [x] Add Readme.md
- [x] Add LRU cache
- [ ] Add LFU cache
- [ ] Add MRU cache
- [x] Add FIFO cache
- [ ] Add LIFO cache

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

This repository and all its content is under `GNU General Public License v3.0`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
