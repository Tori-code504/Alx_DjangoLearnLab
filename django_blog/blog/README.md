## Blog Post Management (CRUD)

- **List** `/posts/`: Everyone can view all posts (paginated).
- **Detail** `/posts/<pk>/`: Everyone can view a single post.
- **Create** `/posts/new/`: Authenticated users only. Author is set to the logged-in user automatically.
- **Edit** `/posts/<pk>/edit/`: Only the post’s author.
- **Delete** `/posts/<pk>/delete/`: Only the post’s author.

### How to Use
1. Log in at `/accounts/login/`.
2. Click “New Post” on the posts list to create.
3. Use the “Edit”/“Delete” buttons on your own posts.

### Notes
- Uses Django class-based views: `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`.
- `LoginRequiredMixin` prevents unauthenticated creation/edits.
- `UserPassesTestMixin` ensures only the author can edit/delete.
- Messages provide user feedback on create/update/delete.

## Comment System
- **View comments:** Everyone can read comments under posts.
- **Add comment:** Authenticated users only. Form is shown under each post.
- **Edit/Delete comment:** Only the comment’s author.
- **URLs:**
  - Add: `/posts/<post_id>/comments/new/`
  - Edit: `/comments/<comment_id>/update/`
  - Delete: `/comments/<comment_id>/delete/`

