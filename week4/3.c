#include <stdio.h>
typedef struct student {
	int id;
	char* pname;
	double points;
} STUD;

void stud_print(STUD* ps);
void stud_swap(STUD* a, STUD* b);
STUD* stud_get_last(STUD* ps_array);
int stud_compare_points(STUD* ps1, STUD* ps2);

void stud_bubble_sort(STUD* pnuecs) {
	int num = 0, num2 = 0;
	int i, j;
	STUD* ps;

	for (ps = pnuecs; ps->id >= 0; ps++) {
		//stud_print(ps);
		num++;
	}

	//printf("%d\n", num);	
	for (i = 0; i < num + 1; i++) {
		for (j = 0; j < num; j++) {
			if ((pnuecs + j)->points < (pnuecs + (j + 1))->points) {
				stud_swap(pnuecs + j, pnuecs + j + 1);
			}
		}
	}

	return;
}


int main(void) {
	STUD pnuecs[] = { {1, "Choi", 9.9}, {2, "Park", 0.1},
		{3, "Kim", 5.0 }, {4, "Lee", 3.0 }, {5, "Moon", 9.5 },
		{6, "Kang", 7.0 }, {7, "Jeon", 0.9 }, {-1, NULL, 0 } };

	STUD* ps_cur = pnuecs;
	int test_id = 0;
	scanf("%d", &test_id);
	if (test_id) set_values_of_pnuecs(pnuecs, test_id);

	stud_bubble_sort(pnuecs);

	while (ps_cur->id > 0)
		stud_print(ps_cur++);

	return 0;
}

void set_values_of_pnuecs(STUD* pnuecs, int test) {
	STUD pnuecs1[] = { {1, "Choi", 3.9}, {2, "Park", 2.1},
		{3, "Kim", 9.0 }, {4, "Lee", 3.5 }, {5, "Moon", 4.5 },
		{6, "Kang", 2.0 }, {7, "Jeon", 8.9 }, {-1, NULL, 0 } };
	STUD pnuecs2[] = { {1, "Choi", 2.5}, {2, "Park", 4.1},
		{3, "Kim", 1.0 }, {4, "Lee", 8.0 }, {5, "Moon", 8.5 },
		{6, "Kang", 5.0 }, {7, "Jeon", 3.9 }, {-1, NULL, 0 } };
	STUD* pnew = (test % 2) ? pnuecs1 : pnuecs2;
	int i = 0;

	while (i < 7) {
		pnuecs[i] = pnew[i];
		i++;
	}
}



void stud_print(STUD* ps) {
	printf("[%d:%s] = %lf\n", ps->id, ps->pname, ps->points);
}

void stud_swap(STUD* a, STUD* b) {
	STUD buf;
	buf = *a;
	*a = *b;
	*b = buf;
}

STUD* stud_get_last(STUD* ps_array) {
	while (ps_array->id >= 0) {
		ps_array++;
	}
	return --ps_array;
}

int stud_compare_points(STUD* ps1, STUD* ps2) {
	// Enter your code here
	int ret = 1;
	if (ps1->points < ps2->points)
		ret = -1;
	else if (ps1->points == ps2->points)
		ret = 0;
	return ret;
}

STUD* stud_get_lowest_points(STUD* ps_begin, STUD* ps_end) {
	STUD* plowest = ps_begin++;

	if (ps_end) {	// ps_end is not NULL
		while (ps_begin <= ps_end) {
			if (stud_compare_points(ps_begin, plowest) < 0)
				plowest = ps_begin;
			ps_begin++;
		}
	}
	else {			// ps_end is NULL
		while (ps_begin->id >= 0) {
			if (stud_compare_points(ps_begin, plowest) < 0)
				plowest = ps_begin;
			ps_begin++;
		}
	}
	return plowest;
}