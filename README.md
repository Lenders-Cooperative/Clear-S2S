<h1 align="center">KYC Clear S2S</h1>


<p align="center"> A module for Thomson Reuters ClearID System to System search.
    <br> 
</p>

### Installing

```
pip install django-clear-s2s
```

```python
>>> from clear_s2s.ThomsonReuters import ThomsonReuters
>>> client = ThomsonReuters('host', 'username_if_avaliable', 'password_if_avaliable', 'client_id', 'client_secret', 'scopes')
>>> _dict = {
        'first_name':'JANE',
        'last_name':'SAMPLE-DOCUMENT',
        'dob':'1951-01-01',
        'ssn':'999-99-9990',
        'street':'240 Summit Avenue',
        'city':'Saint Paul',
        'state':'MN',
        'zip_code':'55102',
        'phone_number':'651-396-0726',
        'npi_number':'9999999999'
    }  
>>> client.person_search(_dict)
OrderedDict([('ns3:PersonResultsPage', OrderedDict([('@xmlns:ns3', 'http://clear.thomsonreuters.com/api/search/2.0'), ('Status', OrderedDict([('StatusCode', '200'), ('SubStatusCode', '200')])), ('StartIndex', '0'), ('EndIndex', '0'), ('ResultGroup', OrderedDict([('GroupId', '8a4d0084720e7ef201720efc1b84307c'), ('RecordCount', '1'), ('Relevance', '99'), ('DominantValues', OrderedDict([('ns2:PersonDominantValues', OrderedDict([('@xmlns:ns2', 'com/thomsonreuters/schemas/search'), ('Name', OrderedDict([('FirstName', 'JANE'), ('LastName', 'SAMPLE-DOCUMENT')])), ('SSN', '999-99-XXXX'),

...

```