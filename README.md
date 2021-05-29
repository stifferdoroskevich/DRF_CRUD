# DRF_CRUD
## Django Rest Framework - CRUD
Using SQLite

### Model
- Id : pk
- Title : Char (max 200)
- Description : Text
- Completed : Boolean



## To return the endpoints list.
$/api/ 

```bash
'List':'/task-list/',
'Detail View':'/task-detail/<str:pk>/',
'Create':'/task-create/',
'Update':'/task-update/<str:pk>/',
'Delete':'/task-delete/<str:pk>/',
```
