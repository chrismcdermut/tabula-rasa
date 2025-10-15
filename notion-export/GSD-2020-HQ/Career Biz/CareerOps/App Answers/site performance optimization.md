# site performance optimization

Answer: • -Reduce bundle size through minification, compression and then code split so bundles are only loaded when needed.
-Separate CSS into its own file for maintainability, but inline critical styles for above-the-fold content to optimize First Contentful Paint (FCP) and ensure users see meaningful content quickly.
-Lazy load data to not overwhelm the client, one small trick is to preempt loading the likely next needed data (like the next page of data) to improve perceived performance.
-Can use memoization within react to avoid unnecessary rerenders
-Apply atomic design principles to break components into reusable, composable, shallow units to simplify render trees and make it more performant.
-Implement virtualization to only render what the user sees.
-For state management, keep state as close to components as possible to prevent prop drilling and unnecessary renders.
• Minification, compression, code splitting, inline CSS for above the fold FCP, lazy loading, memoization, atomic design, virtualization, colocated state
• Reduce bundle size through minification and compression, then apply code splitting to load only what’s needed per route or interaction.
• Separate CSS into its own file for maintainability, but inline critical CSS for above-the-fold content to speed up First Contentful Paint (FCP).
• Lazy load data and components to avoid overwhelming the main thread. Preload likely-needed data (e.g., the next page) for smoother UX.
• Use memoization in React (useMemo, useCallback, React.memo) to avoid unnecessary recalculations and re-renders.
• Apply Atomic Design principles to break components into reusable, shallow, and composable units—making the render tree simpler and more performant.
• Co-locate state near the components that need it to reduce prop drilling and unnecessary renders. For complex flows, use useReducer or selector-driven state stores.
• final

    ◦ Minification, compression, code splitting, inline CSS for above the fold FCP, lazy loading, memoization, atomic design, virtualization, colocated state
Company: Untitled (https://www.notion.so/2316509554a781e687dfeefb9c18e2df?pvs=21)
Question 1: What are some ways to optimize the performance of a website? Mention a few techniques related to JavaScript and React.